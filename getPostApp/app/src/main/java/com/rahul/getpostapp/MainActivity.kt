package com.rahul.getpostapp

import android.content.Intent
import android.os.Bundle
import android.util.Log
import android.widget.*
import androidx.appcompat.app.AppCompatActivity
import com.google.android.gms.tasks.OnSuccessListener
import com.google.firebase.iid.FirebaseInstanceId
import com.google.firebase.iid.InstanceIdResult
import com.rahul.getpostapp.Models.LoginModel
import com.rahul.getpostapp.Models.LoginResponse
import com.rahul.getpostapp.Models.NullClass
import com.rahul.getpostapp.Models.SignupModel
import kotlinx.android.synthetic.main.courses_page.*
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

/*
private val String.isInitialized: Boolean
    get(){
    return String!=null
}
*/
class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        /*lateinit var Token:String
        FirebaseInstanceId.getInstance().instanceId.addOnSuccessListener(this@MainActivity, OnSuccessListener<InstanceIdResult> { instanceIdResult ->
            val newToken = instanceIdResult.token
            Token = newToken
            //Log.e("newToken", newToken)
        })*/
        val user: EditText = findViewById<EditText>(R.id.editTextPersonName)
        val pass: EditText = findViewById<EditText>(R.id.editTextPassword)
        val Email: EditText = findViewById<EditText>(R.id.editTextEmailAddress)
        val signInButton = findViewById<Button>(R.id.signInButton)
        val signUpButton = findViewById<Button>(R.id.signupButton)

        val retrofit = Retrofit.Builder()
                .baseUrl("http://192.168.55.106:8000/")
                .addConverterFactory(GsonConverterFactory.create())
                .build()
        var apiinterface = retrofit.create(ApiInterface::class.java)

        signInButton.setOnClickListener {

            val sharedpreferences = getSharedPreferences("TOKEN", MODE_PRIVATE)
            val token: String? =sharedpreferences.getString("TOKEN", "")

            if(user.text.toString().isEmpty() || pass.text.toString().isEmpty() || Email.text.toString().isEmpty())
                Toast.makeText(this, "Email Address or Password is not provided",  Toast.LENGTH_LONG).show()
            else {
                val username = user.text.toString()
                val password = pass.text.toString()
                val email = Email.text.toString()

                    val signInModel = LoginModel(username, email, password, true, false, token)
                    val call: Call<LoginResponse> = apiinterface.loginUser(signInModel)
                    call.enqueue(object : Callback<LoginResponse> {
                        override fun onResponse(
                                call: Call<LoginResponse>,
                                response: Response<LoginResponse>
                        ) {
                            if (!response.isSuccessful) {
                                val message = response.code().toString()
                                Toast.makeText(applicationContext, "Error encountered", Toast.LENGTH_SHORT).show()
                                //error.setText(response.code().toString())
                                return
                            }
                            val loginresponse = response.body()
                            val sharedPreferences = getSharedPreferences("jwt_token", MODE_PRIVATE)
                            val editor = sharedPreferences.edit()
                            editor.apply {
                                if (loginresponse != null) {
                                    putString("jwt_token", loginresponse.getJWT())
                                }
                            }.apply()
                            val message = loginresponse?.getJWT()
                            Toast.makeText(applicationContext, "Logged in", Toast.LENGTH_SHORT).show()
                            val intent = Intent(getBaseContext(), CoursespageActivity::class.java)
                            //intent.putExtra("userName", response.body()!!.getJWT());
                            startActivity(intent)
                            finish()
                        }

                        override fun onFailure(call: Call<LoginResponse>, t: Throwable) {
                            t.printStackTrace()
                        }
                    })

            }
        }

        signUpButton.setOnClickListener{
            if(user.text.toString().isEmpty() || pass.text.toString().isEmpty() || Email.text.toString().isEmpty()) {
                Toast.makeText(this, "Email Address or Password is not provided", Toast.LENGTH_LONG)
                    .show()
            }
            else {
                val username = user.text.toString()
                val password = pass.text.toString()
                val email = Email.text.toString()
                val signUpModel = SignupModel(username, email, password)
                val call: Call<NullClass> = apiinterface.signupUser(signUpModel)
                call.enqueue(object : Callback<NullClass> {
                    override fun onResponse(call: Call<NullClass>, response: Response<NullClass>) {
                        if (!response.isSuccessful()) {
                            val message = response.code().toString()
                            Toast.makeText(applicationContext,message,Toast.LENGTH_SHORT).show()
                            //error.setText(response.code())
                            return
                        }
                        val message = response.code().toString()
                        Toast.makeText(applicationContext, "Signed Up", Toast.LENGTH_SHORT)
                                .show()
                    }
                    override fun onFailure(call: Call<NullClass>, t: Throwable) {
                        //Toast.makeText(applicationContext,"SignUp failed {t.getmessage()}",Toast.LENGTH_SHORT).show()
                        t.printStackTrace()
                    }
                })
            }
        }
    }
}