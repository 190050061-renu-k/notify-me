package com.rahul.getpostapp.Models

class LoginModel(username:String, email:String, password:String,is_student:Boolean, is_instructor:Boolean, registration_token:String?) {
    val username:String
    private val email:String
    private val password:String
    private val is_student:Boolean
    private val is_instructor:Boolean
    private val registration_token:String?

    init{
        this.username = username
        this.email = email
        this.password=password
        this.is_student=is_student
        this.is_instructor=is_instructor
        this.registration_token=registration_token
    }
}