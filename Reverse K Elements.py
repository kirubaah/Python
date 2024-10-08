def reverse_k_elements(lst, k):
    result = []
    for i in range(0, len(lst), k):
        chunk = lst[i:i + k]
        result.extend(chunk[::-1])
    return result

k = int(input("K: "))
lst = list(map(int, input("Input (separated by hyphens): ").split('-')))
result = reverse_k_elements(lst, k)
print("Output:", ' - '.join(map(str, result)))