#include <Windows.h>
#include <stdio.h>

int main() {
	PVOID pBaseAddress = nullptr;
	CHAR cbuffer[] = "We are in the heap!";

	HANDLE hProcessHeap = GetProcessHeap();
	pBaseAddress = HeapAlloc(hProcessHeap, HEAP_ZERO_MEMORY, 0x100); // Assign 256 bytes of memory on Heap

	printf("Base Address: %p\n\n", pBaseAddress);
	memcpy(pBaseAddress, &cbuffer, sizeof(cbuffer));
	RtlFillMemory((LPTSTR)((UINT64)pBaseAddress + sizeof(cbuffer)-1), (256 - sizeof(cbuffer)+1), 'A');

	ULONGLONG ulBaseAddress = (ULONGLONG)pBaseAddress;
	LPTSTR lpBaseAddress = (LPTSTR)(ulBaseAddress);
	for (int i = 0; i < (256/2); i++) {
		if (i % 4 == 0)
			printf(
				"[%d]\t%p:\t0x%X%X%X%X\n", i, (LPTSTR)(ulBaseAddress + i),
				lpBaseAddress[i+3],
				lpBaseAddress[i+2],
				lpBaseAddress[i + 1],
				lpBaseAddress[i]
			);
	};
	HeapFree(hProcessHeap, 0, pBaseAddress);
	getchar();
}