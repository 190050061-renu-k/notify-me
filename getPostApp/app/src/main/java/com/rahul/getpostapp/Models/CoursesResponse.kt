package com.rahul.getpostapp.Models

class CoursesResponse {
    lateinit var code:String
    lateinit var students:List<String>
    lateinit var instructor:String
    lateinit var date:String
    lateinit var name:String

    fun getcode(): String {
        return code
    }
}