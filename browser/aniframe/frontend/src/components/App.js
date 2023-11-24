import Header from "./Header"
import Footer from "./Footer"
import Editor from "./Editor"
import P5 from "./P5"
// import Code from "./Codes";
// import { Editor } from "ace-builds";

function App() {
    
  return (
    
    <div className='App'>
      <Header />

      {/* <div className="app-body"> */}
        <Editor />
        {/* <P5 
          code={pyOutput} // passed props value
        /> */}
        {/* <Code /> */}
        {/* <Footer /> */}
      {/* </div> */}
    </div>
  );
}

export default App;
