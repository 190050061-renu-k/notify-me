package com.rahul.getpostapp.Models

import com.google.gson.annotations.Expose
import com.google.gson.annotations.SerializedName

class SignupModel(username:String, email: String, password:String){
    val username:String
    val email:String
    val password:String
    init{
        this.username = username
        this.email = email
        this.password = password
    }
}