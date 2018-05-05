let inquirer = require("inquirer");
let clear = require("clear");

let data = []
for(let i = 0; i < 256; i++){
	data.push(0);
}

let pointer = 0;

function handle(query){
	query.forEach((val, index) => {
		switch(val){
			case "+":
				(data[pointer] === 255) ? data[pointer] = 0 : data[pointer]++;
				break;
			case "-":
				(data[pointer] === 0) ? data[pointer] = 255 : data[pointer]--;
				break;
			case ">":
				(pointer === 255) ? pointer = 0 : pointer++;
				break;
			case "<":
				(pointer === 0) ? pointer = 255 : pointer--;
				break;
			case ".":
				console.log(String.fromCharCode(data[pointer]));
		}
	})
}

if(process.argv[2]){
	handle(process.argv[2].split(""));
} else{
	clear();
	inquirer.prompt([
			{
				name: "query",
				message: ": "
			}
		])
		.then(ans => {
			handle(ans.query.split(""));
		})
}

