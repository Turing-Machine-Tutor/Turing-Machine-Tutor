export function mapToObject<K extends string | number, V>(x: Map<K, V>): Record<K, V> {
    return Object.fromEntries(x.entries()) as Record<K, V>;
}

export function deepMapToObject(obj: any): any {
    if(typeof(obj) !== "object") {
        return obj;
    }

    if(Array.isArray(obj)) {
        return obj.map(deepMapToObject);
    }

    let entries: [any, any][] = obj instanceof Map ? [...obj.entries()] : Object.entries(obj);

    return Object.fromEntries(entries.map((tpl: any) => [tpl[0], deepMapToObject(tpl[1])]));
}

