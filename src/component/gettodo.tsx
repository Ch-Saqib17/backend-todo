import axios from "axios";
import React from "react";
interface IData {
  id: number;
  name: string;
}
const Baseurl: string = "http://127.0.0.1:800042";

const GetTodo = async () => {
  const data: IData[] = await axios.get(`${Baseurl}/`);
  return (
    <div>
      {data.map((item) => (
        <div>
          <div>{item.name}</div>
        </div>
      ))}
    </div>
  );
};

export default GetTodo;
