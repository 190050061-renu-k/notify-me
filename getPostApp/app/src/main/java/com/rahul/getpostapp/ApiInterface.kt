package com.rahul.getpostapp


import com.rahul.getpostapp.Models.*
import retrofit2.Call
import retrofit2.http.*

interface ApiInterface {

    @POST("dashboardapi/students")
    fun signupUser(@Body signupModel: SignupModel):Call<NullClass>

    @POST("login/")
    fun loginUser(@Body loginModel: LoginModel):Call<LoginResponse>

    @GET("dashboardapi/courses")
    fun courseInfo(@Header("Authorization") authToken:String?):Call<List<CoursesResponse>>

    @POST("dashboardapi/addStudenttoCourse")
    fun joinCourse(@HeaderMap headers: Map<String,String?>,@Body joinCourseModel:JoinCourseModel):Call<NullClass>
    @POST("dashboardapi/courses")
    fun getCourses(@HeaderMap headers: Map<String, String?>):Call<List<deadlineModel>>

}