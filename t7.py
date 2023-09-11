command=input('>')
started=False
stopped=True
while  command.upper() !='QUIT':
    if command.upper()=='STOP':
        if stopped:
            print('Car is already stopped')
        else:
            stop=True
            print('Car stopped')
        command = input('>')

    elif command.upper()=='START':

        if started:
            print("Car is already started")
        else:
            started=True
            print('Car started ... Ready to go')
        command = input('>')

    elif command.upper() == 'HELP':
        print('start- to start the car')
        print('stop-to stop the car')
        print('quit-to exit')
        command = input('>')
    else:
        print("I don't understand that... ")



        command = input('>')




