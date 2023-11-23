import React, {useState, useEffect} from "react";
import AceEditor from "react-ace";
import axios from "axios";
import List from "./List"
import pyCode from '../python/try.py';
import pyCode2 from '../python/convert.py';

// sample import for setting default text from external file
// import { IntegrationTests } from "./example-input";

import "brace/theme/monokai";
import P5 from "./P5";

function Editor(){

    // state for ace editor
    const [editorCode, setEditorCode] = useState("");

    // state for hidden textarea
    const [txtAreaCode, setTxtAreaCode] = useState({
      code: ""
    })

    // state for saving and retrieving codes in db
    const [codes , setNewCodes] = useState(null);

    // loads Pyodide then runs python code; see https://github.com/xhluca/react-pyodide-template/blob/main/src/App.js
    const runPyCode = async (py_code) => {
      
      const pyodide = await window.loadPyodide({
        indexURL : "https://cdn.jsdelivr.net/pyodide/v0.24.1/full/"
      });

      // opens file explorer for selecting dir
      const dirHandle = await window.showDirectoryPicker();

      if ((await dirHandle.queryPermission({ mode: "readwrite" })) !== "granted") {
        if (
          (await dirHandle.requestPermission({ mode: "readwrite" })) !== "granted"
        ) {
          throw Error("Unable to read and write directory");
        }
      }

      // mounts selected dir
      const nativefs = await pyodide.mountNativeFS("/mount_dir", dirHandle);

      // return await pyodide.runPython(py_code);
      await pyodide.runPython(py_code);


      // get python function from py_code
      const convertAnf = pyodide.globals.get("convertAnf");

      // runs the python function itself with passed param
      convertAnf(txtAreaCode.code)
      
      // saves changes made by python function to file in dir 
      await nativefs.syncfs();

    }

    // allows loading of Pyodide and running python code
    const runPy = async () => {
      const runCode = await (await fetch(pyCode2)).text();
      // const out = await runPyCode(runCode);

      await runPyCode(runCode);
    }

    
    // updates the editor contents upon every entered key
    function onChange(newValue) {
      setEditorCode(newValue);
        
        //copies editor contents into hidden textarea for saving to db
        setTxtAreaCode((txtAreaCode) => ({
            ...txtAreaCode, // copies properties of textarea state
            code: newValue}) // update textarea state value
        )

    }

    // resets the editor and textarea contents to be empty
    const resetCode = () => {
      setEditorCode("");
      setTxtAreaCode(({
        code: ""}))
    }

    // pefroms db content retrieval upon loading of site
    useEffect(() => {
      getCodes()
        } ,[])
      
    // retrieves list of contents from db
    function getCodes() {
      axios({
          method: "GET",
          url:"/codes/",
        }).then((response)=>{
          const data = response.data
          setNewCodes(data);

          console.log("LAST ELEM: ", data[data.length-1]);
          
        }).catch((error) => {
          if (error.response) {
            console.log(error.response);
            console.log(error.response.status);
            console.log(error.response.headers);
            }
        })}

    // sends axios post request to save input in db
    function createCode(event) {
        axios({
          method: "POST",
          url:"/codes/",
          data:{
            code: txtAreaCode.code
           }
        })
        .then((response) => {
          // execute python function for conversion
          runPy();

          // get updated codes from db
          getCodes();
        })

        event.preventDefault();
    }

    // deletes an item in the db
    function DeleteCode(id) {
        axios({
          method: "DELETE",
          url:`/codes/${id}/`,
        })
        .then((response) => {
          getCodes()
        })
    }

    return(
      <div className="app-body">
        <div class="editor">
            <form className="editor-code">
                <AceEditor
                    focus="true"
                    value={editorCode}
                    width="100%"
                    fontSize={16}
                    placeholder="Enter anf code here..."
                    wrapEnabled="true"
                    highlightActiveLine="true"
                    showGutter="true"
                    theme="monokai"
                    onChange={onChange}
                    name="ace-editor"
                    setOptions={{
                    enableLiveAutocompletion: true,
                    showLineNumbers: true,
                    }}
                    editorProps={{ $blockScrolling: true }}

                />

                <textarea className="editor-txt" onChange={onChange} name="code" value={txtAreaCode.code} spellCheck="false"/>

                <div class="btn-div">
                    <button onClick={createCode} class="btn submit-btn">Submit</button>
                    <button onClick={resetCode} class="btn reset-btn">Reset</button>
                </div>

            </form>
            
            { codes && codes.map(code => <List
                  key={code.id}
                  id={code.id}
                  code={code.code} 
                  deletion ={DeleteCode}
                />
            )}
           
        </div>

        <P5
          // code = {p5Code}
        />
        
      </div>
        
        
    )


}

export default Editor;