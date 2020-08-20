print("Enter the two no. to add")
print(int(input())+(int(input())))


'''
Converting .py to .exe:
We will discuss the process of converting a python i.e., the .py file into an executable or .exe file. Let us 
start with the introduction of the .exe file. In windows, .exe is an extension used for executable files. It is one 
of the most common file extensions used for almost all kinds of software and applications programs and also setups. 

Now let’s come to the purpose of the conversion. We create lots of Python programs and want to share it with the 
world. If we're going to convert our python program into an application that can be run in any computer without the 
IDE or even installing Python itself, we must convert it to .exe. All the apps and programs we use in our computer 
are written using some language or code, but we do not have to install the particular language for the program to run. 


Steps to Create an Executable from Python Script using Pyinstaller:

Step 1: Install the Pyinstaller Package:
    The first step is to install the module pyinstaller. For this, we will create or destinate a folder and open our 
power shell window there using shift + mouse right-click. 

Now we will run the following command for our module installation.
    pip install pyinstaller
    
Step 2: Save your Python Script:
    Right-click on the screen and then new and text document to create a .txt file and write the python script. We can 
save our python script in a text file, too, for the conversion, it does not necessarily have to be a .py file, 
but the code in it should be of Python. Now open the power shell window and write the following commands. 

python .\main.txt
the code written in the main.txt file will execute.

Step 3: Create the Executable using Pyinstaller:
    As we want a .exe file. So we are going to run the following command.
    
pyinstaller main.txt

It will show us a few warnings, as shown in the image below. Along with that, it could be a little time-consuming in 
case of bigger programs. We should not avoid the warnings as they can be a security threat later on. You can search 
for the meaning of the given warning by searching it on the internet. Sometimes software causes problems while 
installing the pyinstaller module. The reason for this might be the incomplete installation of pip.

Step 4: Run the Executable:
    After running pyinstaller main.txt command, it will create some folders. Click on the dist folder and then click on 
the main.

In that folder, we can find our .exe file. We can open it through the PowerShell window by running the command

.\main.exe

Now, as you saw that by converting the file to .exe, we got several files in the folder, but we can also run a 
command that will provide us with only one file as a resultant. It will take more time in creation and later on it 
will extract too, but for compatibility, we can use the following command: 

pyinstaller --onefile file.py

Here the file extension depends on your file that whether you created it using .py or .txt.

Once we click on the file, we are ready to launch our program.
'''