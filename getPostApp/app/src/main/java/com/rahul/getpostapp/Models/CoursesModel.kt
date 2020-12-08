package com.rahul.getpostapp.Models

class CoursesModel(val code:String?) {
    var coursecode:String?
    init{
        this.coursecode=code
    }
    fun getcode(): String? {
        return coursecode
    }
}