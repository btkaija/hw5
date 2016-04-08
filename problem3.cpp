#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
		
	string line;
	ifstream myfile;
	myfile.open("/etc/passwd");
	if(myfile.is_open()) 
	{
		int pos1, pos2, pos3;
		while( getline (myfile, line ) )
		{
			if(line.find("/bin/bash") != std::string::npos) {
				pos1 = line.find(":");
				pos2 = line.find(":", pos1 +1);
				pos3 = line.find(":", pos2 +1);
				
				cout << line.substr(pos2+1, pos3-pos2-1) << "\t" << line.substr(0, pos1) << endl;
			}
		}
	}
	else cout << "couldn't open file" << endl;
	myfile.close();
}
