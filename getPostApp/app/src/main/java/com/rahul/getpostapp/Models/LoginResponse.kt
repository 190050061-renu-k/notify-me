package com.rahul.getpostapp.Models

class LoginResponse(name:String, token:String) {
        var name:String
        var jwt:String
        init{
            this.name = name
            this.jwt = token
        }
    fun getJWT(): String {
        return jwt
    }

}