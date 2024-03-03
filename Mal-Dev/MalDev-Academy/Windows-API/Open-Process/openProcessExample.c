#include <Windows.h>
#include <stdio.h>
#include <tchar.h>

int main(int argc, char** argv) {
	HANDLE hProcess;
	int id;
	if (argc < 2) {
		printf("Process Id required!\nTry: %s {PROCESS ID}\n", argv[0]);
		return -1;
	}
	printf("Searching proccess: %s\n", argv[1]);
	id = atoi(argv[1]);
	hProcess = OpenProcess(PROCESS_VM_READ, FALSE, id);
	if (hProcess == NULL) {
		printf("Could not open process: %d\n", id);
	}
	printf("Handle: %x", hProcess);
	Sleep(10000); // sleep 10 seconds so we can see the handle
	CloseHandle(hProcess);
	return 0;
}