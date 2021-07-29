import React from "react";

const Button = (props) => {
    return (
        <div>
            <button className={props.classname + " button"} onClick={props.onClick}>{props.name}</button>
        </div>
    )
}

export default Button