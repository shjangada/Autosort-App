from flask import Flask, render_template, request, redirect
import pexpect, sys, pandas as pd
import os
from flask_bootstrap import Bootstrap
import subprocess
from datetime import date

today = date.today()
today = str(today)

app = Flask(__name__)
bootstrap = Bootstrap(app)


# Define a global variable
app.config['HOST'] = 'localhost'
app.config['PIN'] = '12345'
app.config['USER'] = 'pi'

 ### test if redirect works
@app.route('/selection',methods=['GET', 'POST'])
def selection():
    global f 
    f = open('SortSettings.txt', 'r')

    global content
    content = f.read()

    #global line_count
    #line_count = len(f.readlines())

    #param1 = request.args.get('output')
    #return render_template('button.html?output=' + param1)
    print("In Selection Page : " )
    return render_template('button.html')
#########

@app.route('/sort', methods=['GET', 'POST'])
def sort(): 
    #subprocess.Popen("ssh pi@192.168.0.213", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    #os.system("ssh pi@192.168.0.213 'cd autosort' 'python3 test.py'")

    f = open('SortSettings.txt', 'r')
    data = f.read()
    #print("data: " + data)
    valuelist = data.splitlines()
    print(valuelist)
    c1, c2, c3, c4 = [valuelist[i] for i in (0, 1, 2, 3)]

    d = open('SizeSettings.txt', 'r')
    size = d.read()

    global cmmd 
    cmmd = ("python3 /home/pi/autosort/slow.py --c1 " + str(c1) + " --c2 " + str(c2) + " --c3 " + str(c3) + " --c4 " + str(c4) + " --size " + str(size))
    #print(cmmd)

    import paramiko

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('192.168.28.45', username='pi', password='AutoSORT123')

    stdin, stdout, stderr = client.exec_command('sudo pigpiod')
    #stdin, stdout, stderr = client.exec_command('cd autosort')
    stdin, stdout, stderr = client.exec_command(cmmd)
    stdin, stdout, stderr = client.exec_command('python3 /home/pi/autosort/test.py')
    stdin, stdout, stderr = client.exec_command('python3 /home/pi/autosort/vramp.py')
    #stdin, stdout, stderr = client.exec_command('python3 autosort/test.py')

    stdin.close()

    #for line in stdout:
    #    print(line.strip('\n'))

    client.close()


    return render_template('sort.html')


### test if redirect works
@app.route('/report',methods=['GET', 'POST'])
def report():
     # Read the CSV file
    df = pd.read_csv('data.csv')

    # Convert the DataFrame to HTML table
    table = df.to_html(index=False)

    return render_template('report.html', table=table)
#########

@app.route('/RedButton',methods=['GET', 'POST'])
def RedButton():
    if "red" in content:
        return redirect('/ColorError')
    else:
        f = open('SortSettings.txt', 'a')
        f.write('red\n')
        f.close()
        return redirect('/selection')

@app.route('/BlueButton',methods=['GET', 'POST'])
def BlueButton():
    if "blue" in content:
        return render_template('ColorError.html')
    else:
        f = open('SortSettings.txt', 'a')
        f.write('blue\n')
        f.close()
        return redirect('/selection')
    
@app.route('/OrangeButton',methods=['GET', 'POST'])
def OrangeButton():
    if "orange" in content:
        return render_template('ColorError.html')
    else:
        f = open('SortSettings.txt', 'a')
        f.write('orange\n')
        f.close()
        return redirect('/selection')

@app.route('/PinkButton',methods=['GET', 'POST'])
def PinkButton():
    if "pp" in content:
        return render_template('ColorError.html')
    else:
        f = open('SortSettings.txt', 'a')
        f.write('pp\n')
        f.close()
        return redirect('/selection')
        
@app.route('/GreenButton',methods=['GET', 'POST'])
def GreenButton():
    if "green" in content:
        return render_template('ColorError.html')
    else:
        f = open('SortSettings.txt', 'a')
        f.write('green\n')
        f.close()
        return redirect('/selection')

@app.route('/YellowButton',methods=['GET', 'POST'])
def YellowButton():
    if "yellow" in content:
        return render_template('ColorError.html')
    else:
        f = open('SortSettings.txt', 'a')
        f.write('yellow\n')
        f.close()
        return redirect('/selection')

@app.route('/GreyButton',methods=['GET', 'POST'])
def GreyButton():
    if "bw" in content:
        return render_template('ColorError.html')
    else:
        f = open('SortSettings.txt', 'a')
        f.write('bw\n')
        f.close()
        return redirect('/selection')
    
@app.route('/Small',methods=['GET', 'POST'])
def Small():
    d = open('SizeSettings.txt', 'w')
    d.write('small')
    d.close()
    return redirect('/selection')
    
@app.route('/Large',methods=['GET', 'POST'])
def LargeL():
    d = open('SizeSettings.txt', 'w')
    d.write('large')
    d.close()
    return redirect('/selection')

@app.route('/ClearColor',methods=['GET', 'POST'])
def ClearColor():
    open('SortSettings.txt', 'w').close()
    return redirect('/selection')

@app.route('/ColorError', methods= ['GET', 'POST'])
def ColorError():
    return render_template('ColorError.html')

@app.route('/LineError', methods= ['GET', 'POST'])
def LineError():
    return render_template('LineError.html')

@app.route('/abort',methods=['GET', 'POST'])
def abort():
    import paramiko

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('192.168.28.45', username='pi', password='AutoSORT123')

    stdin, stdout, stderr = client.exec_command('sudo pigpiod')
    #stdin, stdout, stderr = client.exec_command('cd autosort')
    stdin, stdout, stderr = client.exec_command("python3 /home/pi/autosort/abort.py")
    #stdin, stdout, stderr = client.exec_command('python3 autosort/test.py')

    stdin.close()

    #for line in stdout:
    #    print(line.strip('\n'))

    client.close()

    return redirect('/selection')

### Login Page ###
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve the input values from the form
        host = request.form.get('hostname')
        pin = request.form.get('pin')
        app.config['HOST'] = request.form.get('hostname')
        app.config['PIN'] = request.form.get('pin')
        # Perform any required processing on the input values
        hostname = app.config['HOST']
        username = app.config['USER']
        password = app.config['PIN']
        command = 'echo "abc" >> /tmp/new.txt'
        try:
            # Spawn an SSH child process
            #ssh = pexpect.spawn(f'ssh {username}@{hostname}')
            spawn = pexpect.spawnu if sys.version_info[0] >= 3 else pexpect.spawn
            #ssh = spawn('ssh -t shreya@127.0.0.1 bash --noprofile --norc')
            #ssh = spawn('ssh -t shreya@' + hostname + ' bash --noprofile --norc')
            ssh = spawn('ssh -t ' + username + '@' + hostname + ' bash --noprofile --norc')

            # Expect password prompt
            #password_prompt = ssh.expect(['password:', 'Permission denied'])
            #ssh.logfile_read = sys.stdout
            password_prompt = ssh.expect('assword:')
            #ssh.sendline('123456')
            
            if password_prompt == 0:
                # Send the password
                ssh.sendline(password)
                # Expect command prompt
                #ssh.expect(f'{username}@')
                ssh.expect('bash-[.0-9]+[$#]')
                print("correct password. SSH connection success.")
                # Send the command
                ssh.sendline(command)

                # Expect the command output
                #ssh.expect(f'{username}@')
                ssh.expect('bash-[.0-9]+[$#]')

                # Print the output of the command
                #print(ssh.before.decode())
                #print(ssh.before)
                output = ssh.before
                # Close the SSH connection
                ssh.close()
                # Print output
                #return redirect('/result?output=' + output)
                return redirect('/selection')
                #output = "Success"
                #return redirect('/selection?output=' + output)
            
            elif password_prompt == 1:
                # Handle wrong password
                print("Incorrect password. SSH connection failed.")

        except pexpect.EOF:
            # Handle the end of file error
                print("SSH connection terminated unexpectedly.")

        except pexpect.TIMEOUT:
            # Handle timeout error
            print("SSH connection timed out.")
        # Return a response or redirect to another page
        return "Either the username or password entered is incorrect. \nReceived input values: Host Address = {}, PIN = {}".format(host, pin)
    
        # If it's a GET request, render the template with the input form
    return render_template('index.html')

   
    
if __name__ == '__main__':
    app.run()
