package com.rahul.getpostapp.Models

class deadlineModel(code:String,instructor:String,date:String,instructor_name:String,list:List<String>) {
    private val code:String
    private val instructor:String
    private val date:String
    private val instructor_name: String
    private val students_list: List<String>
    init{
        this.code = code
        this.instructor = instructor
        this.date = date
        this.instructor_name = instructor_name
        this.students_list = list
    }
}