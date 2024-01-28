import { FormEvent, useState } from "react";
import { CodeRequestBody, CodeResponseBody } from "../../shared/dto/turing-api";

const initialCode = `
def build():
    # Example Turing Machine parameters
    input_alphabet = ['0', '1']
    tape_alphabet = ['0', '1', 'B']  # B represents blank symbol
    blank = 'B'
    states = ['q0', 'q1', 'acc', 'rej']
    initial_state = 'q0'
    acc = 'acc'
    rej = 'rej'
    delta = {
        ('q0', '0'): ('0', 'q1', 'R'),
        ('q0', '1'): ('1', 'q1', 'R'),
        ('q1', '0'): ('0', 'q0', 'L'),
        ('q1', '1'): ('1', 'q0', 'L'),
        ('q0', 'B'): ('B', 'acc', 'S'),
        ('q1', 'B'): ('B', 'rej', 'S')
    }

    return {
        'input_alphabet': input_alphabet,
        'tape_alphabet': tape_alphabet,
        'blank': blank,
        'states': states,
        'initial_state': initial_state,
        'acc': acc,
        'rej': rej,
        'delta': delta
    }`

export default function MyForm() {
    const [codeInput, setCodeInput] = useState(initialCode);
  const [result, setResult] = useState<Record<string, unknown>>({});
  const [disabled, setDisabled] = useState(false);

  const handleCodeSubmit = async (e: FormEvent) => {
    e.preventDefault();
    const request: CodeRequestBody = { code: codeInput };
    try {
      setDisabled(true);
      const response = await fetch('/api/turing', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(request),
      });

      if (response.ok) {
        const data: CodeResponseBody = await response.json();
        setResult(data.result);
      } else {
        console.error('Error:', response.statusText);
      }
    } catch (error) {
      console.error('Error submitting code:', error);
    } finally {
      setDisabled(false);
    }
  };

  return (
    <div>
      <form onSubmit={handleCodeSubmit}>
        <label>
          Enter Code:
          <textarea
            value={codeInput}
            onChange={(e) => setCodeInput(e.target.value)}
            rows={5}
            cols={40}
          />
        </label>
        <br />
        <button type="submit" disabled={disabled}>Submit Code</button>
      </form>

      {result && (
        <div>
          <h3>Result:</h3>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}