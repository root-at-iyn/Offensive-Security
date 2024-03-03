#include <Windows.h>
#include <tchar.h>
#include <stdio.h>


int main() {
	CHAR username[MAXWORD] = {'\0'};
	DWORD pcbBuffer[MAXWORD];

	if (!GetUserNameA((LPSTR)username, (LPDWORD)&pcbBuffer)) {
		DWORD error = GetLastError();
		printf("Error Code: %d\n", error);
		return error;
	};

	printf("Username: %s", username);
	getchar();
}