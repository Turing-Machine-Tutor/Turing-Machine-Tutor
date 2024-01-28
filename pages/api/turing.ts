import type { NextApiRequest, NextApiResponse } from 'next'
import { cwd } from "process"; 
import { CodeRequestBody, CodeResponseBody } from '../../shared/dto/turing-api';
import { loadPyodide } from "pyodide";
import { deepMapToObject } from '../../shared/map-to-obj';


const define_to_js = `


def convert_delta_format(tupledict):
  result = {}
  for (x, y), (nextState, write, move) in tupledict.items():
    if x not in result:
      result[x] = {}
    result[x][y] = {"nextState": nextState, "write": write, "move": move}
  return result

def to_js_object(result):
    # change result so result["delta"] changes from a dict where the key
    # is a tuple, to a dict of dicts.
    result["delta"] = convert_delta_format(result["delta"])
    return result
`


export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  const { code } = req.body as CodeRequestBody;
  const pyodide = await loadPyodide();
    let output = "";
    pyodide.setStdout({
        batched: (str: string) => output += str
    });

    await pyodide.runPythonAsync(code);
    const globals: Map<string, any> = pyodide.globals.toJs();
    if(!globals.has("build")) {
      res.status(500).send("build function not found");
    }
    await pyodide.runPythonAsync(define_to_js);
    const result: Map<string, any> = await pyodide.runPythonAsync(`to_js_object(build())`)
    .then(x => x.toJs()).then(deepMapToObject);
    console.log("result", result);

  const resBody: CodeResponseBody = { result: result };
  res.status(200).json(resBody);
}