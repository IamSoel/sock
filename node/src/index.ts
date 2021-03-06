import express from "express"
import PythonShell from "python-shell"
const app=express();

//Router to handle the incoming request.
app.get("/", (req, res, next)=>{
	//Here are the option object in which arguments can be passed for the python_test.js.
	let options:PythonShell.Options = {
		mode: 'text',
		pythonOptions: ['-u'], // get print results in real-time
		scriptPath: '../scrape_scripts/', //If you are having python_test.py script in same folder, then it's optional.
		// args: ['shubhamk314'] //An argument which can be accessed in the script using sys.argv[1]
	};
	
	PythonShell.PythonShell.run('listed_companies.py', options, function (err:PythonShell.PythonShellError, result){
		if (err) throw err;
		// result is an array consisting of messages collected
		//during execution of script.
		console.log('result: ', result.toString());
		res.send(result.toString())
	});
});

//Creates the server on default port 8000 and can be accessed through localhost:8000
const port=8000;
app.listen(port, ()=>console.log(`Server connected to ${port}`));
