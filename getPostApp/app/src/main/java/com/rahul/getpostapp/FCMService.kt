package com.rahul.getpostapp

import android.content.Context
import android.content.Context.MODE_PRIVATE
import android.content.SharedPreferences
import android.provider.Settings.Global.putString
import android.util.Log
import com.google.android.gms.tasks.OnSuccessListener
import com.google.firebase.iid.InstanceIdResult
import com.google.firebase.messaging.FirebaseMessagingService


    //val TAG = "FCM Service: "
    class FCMService : FirebaseMessagingService() {
        /*val TAG = "FCM Service: "
        override fun onNewToken(p0: String) {
            Log.d(TAG, p0)
            saveToken(p0)
            super.onNewToken(p0)
        }

        fun saveToken(token: String) {
            val sharedPreferences = getSharedPreferences("registration_token", MODE_PRIVATE)
            val editor = sharedPreferences.edit()
            editor.apply {
                putString("registration_token", token)
            }
            editor.commit()
        }*/
        override fun onNewToken(s: String): kotlin.Unit {
            super.onNewToken(s)
            Log.d("NEW_TOKEN", s)
            val str = s
            val sharedPreferences = getSharedPreferences("login", Context.MODE_PRIVATE)
            val editor: SharedPreferences.Editor = sharedPreferences.edit()
            editor.putString("TOKEN", str)
            Log.d("token", str)
            editor.apply()
            editor.commit()
            val t = sharedPreferences.getString("TOKEN","")
            Log.d("shared",t.toString())
        }
    }
