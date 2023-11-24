function List(props){

    function handleClick(){
      props.deletion(props.id)
    }

  return (
      <div className="code">
        <p >{props.code}</p>
        <button className="btn btn-danger delete-btn" onClick={handleClick}>Delete</button>
      </div>
  )
}

export default List;
