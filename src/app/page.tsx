'use client'

import Image from "next/image";
import { CodeRequestBody, CodeResponseBody } from "../../shared/dto/turing-api";
import MyForm from "./MyForm";

export default function Home() {
  return <MyForm/>;
}