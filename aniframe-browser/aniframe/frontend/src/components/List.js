function List(props){

    function handleClick(){
      props.deletion(props.id)
    }

  return (
      <div className="code">
        {/* <h1 >{props.filename}</h1> */}
        <p >{props.code}</p>
        <button onClick={handleClick}>Delete</button>
      </div>
  )
}

export default List;
