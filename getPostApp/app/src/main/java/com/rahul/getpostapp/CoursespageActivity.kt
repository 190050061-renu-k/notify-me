package com.rahul.getpostapp

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import com.rahul.getpostapp.Models.*
import kotlinx.android.synthetic.main.courses_page.*
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import java.util.ArrayList

class CoursespageActivity : AppCompatActivity() {
    private lateinit var courseadapter: CourseAdapter
    override fun onCreate(savedInstanceState: Bundle?) {

        super.onCreate(savedInstanceState)
        setContentView(R.layout.courses_page)
        val enterCode = findViewById<EditText>(R.id.edit_coursecode)
        var submitButton: Button = findViewById<Button>(R.id.submitButton)
        val listofCourses:Button = findViewById<Button>(R.id.listButton)
        val sharedpreferences = getSharedPreferences("jwt_token", MODE_PRIVATE)
        val token: String? =sharedpreferences.getString("jwt_token", null)

        val retrofit = Retrofit.Builder()
            .baseUrl("http://192.168.55.106:8000/")
            .addConverterFactory(GsonConverterFactory.create())
            .build()
        var apiinterface = retrofit.create(ApiInterface::class.java)
        submitButton.setOnClickListener {

            val code = enterCode.text.toString()
            val joinCourseModel = JoinCourseModel(code)
            val headers  = HashMap<String,String?>()
            headers["Authorization"] = token
            val call:Call<NullClass> = apiinterface.joinCourse(headers,joinCourseModel)
            call.enqueue(object: Callback<NullClass> {
                override fun onResponse(call: Call<NullClass>, response: Response<NullClass>) {
                    if(!response.isSuccessful){
                        return
                    }
                    if(response.code() == 200){
                        Toast.makeText(applicationContext,"Succesfully joined the course",Toast.LENGTH_SHORT).show()
                    }
                    else{
                        Toast.makeText(applicationContext,"Unable to register",Toast.LENGTH_SHORT).show()
                    }
                }

                override fun onFailure(call: Call<NullClass>, t: Throwable) {
                    t.printStackTrace()
                }
            })
        }
        //Toast.makeText(applicationContext, token, Toast.LENGTH_SHORT).show()
        listofCourses.setOnClickListener {

            val headers  = HashMap<String,String?>()
            headers["Authorization"] = token
            val call: Call<List<deadlineModel>> = apiinterface.getCourses(headers)
            call.enqueue(object : Callback<List<deadlineModel>>{
                override fun onResponse(
                    call: Call<List<deadlineModel>>,
                    response: Response<List<deadlineModel>>
                ) {
                    //var courses_list = response.body()
                   // val intent = Intent(getBaseContext(), listCoursesActivity::class.java)
                    //intent.putExtra("course-array", courses_list);
                    //startActivity(intent)
                }
                override fun onFailure(call: Call<List<deadlineModel>>, t: Throwable) {
                    t.printStackTrace()
                }
            })
        }

        //initRecyclerView()
    }
        //adddataset()

    /*private fun adddataset(list:MutableList<CoursesModel>){
        val data = list
        courseadapter.submitList((data))
    }
    private fun initRecyclerView(){
        courseadapter = CourseAdapter()
        recycler_view.layoutManager = LinearLayoutManager(this)
        recycler_view.adapter = courseadapter
    }*/
}