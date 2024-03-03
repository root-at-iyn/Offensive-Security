#include <Windows.h>
#include <stdio.h>

typedef void (WINAPI* fnHelloMaldev)();

int main() {
	HMODULE hModule = GetModuleHandleA("dllExample.dll");
	if (hModule == NULL) {
		hModule = LoadLibraryA("dllExample.dll");
	}
	
	PVOID pHelloMaldev = GetProcAddress(hModule, "HelloMaldev");
	fnHelloMaldev HelloMaldev = (fnHelloMaldev)pHelloMaldev;
	if (HelloMaldev == NULL) {
		printf("Failed to run HelloMaldev: %s", GetLastError());
	}
	else
	{
		HelloMaldev();
	}
}