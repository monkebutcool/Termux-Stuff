const readline = require('readline');
const { exec } = require('child_process');

function clearTerminal() {
    exec('clear', (err) => {
        if (err) {
            console.error(`Error clearing terminal: ${err}`);
        }
    });
}

function displayMenu() {
    console.log("\033[1mMonkeMisc\033[0m");
    console.log("Which one do you want to run?");
    console.log("[1] Force Deleter FDel");
    console.log("[2] Internet Info InternetInfo");
    console.log("[3] Website Up Or Not SiteUpNot");
    console.log("[4] Random IP Generator RandomIPGen");
    console.log("[A] Author");
    console.log("[E] Exit");
}

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function promptUser() {
    displayMenu();
    rl.question("Enter your choice: ", (choice) => {
        clearTerminal();
        switch(choice) {
            case '1':
                exec('python modules/FDel.py', (err, stdout, stderr) => {
                    if (err) {
                        console.error(`Error: ${stderr}`);
                    } else {
                        console.log(stdout);
                    }
                    promptUser();
                });
                break;
            case '2':
                exec('python modules/InternetInfo.py', (err, stdout, stderr) => {
                    if (err) {
                        console.error(`Error: ${stderr}`);
                    } else {
                        console.log(stdout);
                    }
                    promptUser();
                });
                break;
            case '3':
                exec('python modules/SiteUpNot.py', (err, stdout, stderr) => {
                    if (err) {
                        console.error(`Error: ${stderr}`);
                    } else {
                        console.log(stdout);
                    }
                    promptUser();
                });
                break;
            case '4':
                exec('python modules/RandomIPGen.py', (err, stdout, stderr) => {
                    if (err) {
                        console.error(`Error: ${stderr}`);
                    } else {
                        console.log(stdout);
                    }
                    promptUser();
                });
                break;
            case 'A':
            case 'a':
                console.log("Visit: https://apksntermux.blogspot.com/");
                promptUser();
                break;
            case 'E':
            case 'e':
                console.log("Exiting...");
                rl.close();
                break;
            default:
                rl.close();
                break;
        }
    });
}

clearTerminal();
promptUser();
