kotha repo package com.aws_squad.notify

import android.util.Log
import androidx.core.app.NotificationCompat
import com.google.firebase.messaging.FirebaseMessagingService
import com.google.firebase.messaging.RemoteMessage

class FCMService : FirebaseMessagingService() {
    val TAG = "FCM Service: "
    override fun onNewToken(p0: String) {
        Log.d(TAG,p0)
    }
}