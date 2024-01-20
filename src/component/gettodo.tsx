import axios from "axios";
import React from "react";

interface IData {
  id: number;
  name: string;
}

const Baseurl: string = "http://127.0.0.1:8000";

const GetTodo = async () => {
  const response  = await axios.get(`${Baseurl}`);
  const data : IData[] = response.data;
  return (
    <div>
      {data.map((item) => (
        <div key={item.id} >
          <div>{item.name}</div>
        </div>
      ))}
    </div>
  );
};

export default GetTodo;
