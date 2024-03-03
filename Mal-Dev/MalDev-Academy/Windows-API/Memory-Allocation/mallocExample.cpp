#include <Windows.h>
#include <stdio.h>

int main() {
	PVOID pBaseAddress = nullptr;
	CHAR cbuffer[] = "We are in the heap!";

	pBaseAddress = malloc(0x100); // Assign 256 bytes of memory on Heap

	printf("Base Address: %p\n\n", pBaseAddress);
	memcpy(pBaseAddress, &cbuffer, sizeof(cbuffer));

	ULONGLONG ulBaseAddress = (ULONGLONG)pBaseAddress;
	LPTSTR lpBaseAddress = (LPTSTR)(ulBaseAddress);
	for (int i = 0; i < (256/4); i++) {
		if (i % 4 == 0)
			printf(
				"%p:\t0x%X%X%X%X\n", (LPTSTR)(ulBaseAddress + i),
				lpBaseAddress[i],
				lpBaseAddress[i + 1],
				lpBaseAddress[i + 2],
				lpBaseAddress[i + 3]
				);
	};
	free(pBaseAddress);
	getchar();


}