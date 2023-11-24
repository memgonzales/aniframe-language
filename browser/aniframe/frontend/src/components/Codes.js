import {useState, useEffect} from "react";
import axios from "axios";
import List from "./List"
import AddIcon from "@material-ui/icons/Add";

function Code() {
    const [isExpanded, setExpanded]= useState(false)
    const [rows, setRows]= useState(1)

    const [codes , setNewCodes] = useState(null)
    const [formCode, setFormCode] = useState({
      filename: "",
      code: ""
    })

    useEffect(() => {
      getCodes()
        } ,[])

    function getCodes() {
      axios({
          method: "GET",
          url:"/codes/",
        }).then((response)=>{
          const data = response.data
          setNewCodes(data)
        }).catch((error) => {
          if (error.response) {
            console.log(error.response);
            console.log(error.response.status);
            console.log(error.response.headers);
            }
        })}

    function createCode(event) {
        axios({
          method: "POST",
          url:"/codes/",
          data:{
            filename: formCode.filename,
            code: formCode.code
           }
        })
        .then((response) => {
          getCodes()
        })

        setFormCode(({
          filename: "",
          code: ""}))
        setExpanded(false)
        event.preventDefault()
    }

    function DeleteCode(id) {
        axios({
          method: "DELETE",
          url:`/codes/${id}/`,
        })
        .then((response) => {
          getCodes()
        })
    }

    function handleChange(event) { 
        const {value, name} = event.target
        setFormCode(prevCode => ({
            ...prevCode, [name]: value})
        )}

    function CodeShow(){
        setExpanded(true)
        setRows(15)
      }

  return (
    
     <div className='anf-code'>

        <form className="create-code">
          {isExpanded && <input onChange={handleChange} text={formCode.filename} name="filename" placeholder="Filename" value={formCode.filename} />}
          <textarea onClick={CodeShow} onChange={handleChange} name="code" placeholder="Enter code here" rows={rows} cols='10' value={formCode.code} />
          {isExpanded && <button onClick={createCode}>
                            <AddIcon />
                        </button>}
        </form>

        { codes && codes.map(code => <List
        key={code.id}
        id={code.id}
        filename={code.filename}
        code={code.code} 
        deletion ={DeleteCode}
        />
        )}

    </div>

  );
}

export default Code;
