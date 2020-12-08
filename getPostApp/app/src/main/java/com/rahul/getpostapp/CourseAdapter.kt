package com.rahul.getpostapp

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.appcompat.view.menu.ActionMenuItemView
import androidx.recyclerview.widget.RecyclerView
import com.rahul.getpostapp.Models.CoursesModel
import kotlinx.android.synthetic.main.courses_layout.view.*

class CourseAdapter : RecyclerView.Adapter<RecyclerView.ViewHolder>()
{
    private var courses: List<CoursesModel> = ArrayList()

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): RecyclerView.ViewHolder {
        return courseViewHolder(
            LayoutInflater.from(parent.context).inflate(R.layout.courses_layout, parent, false)
        )

        //return RecyclerView.ViewHolder(v)
    }

    override fun getItemCount(): Int {
        return courses.size
    }

    override fun onBindViewHolder(holder: RecyclerView.ViewHolder, position: Int) {
        when(holder){
            is courseViewHolder ->{
                holder.bind(courses.get(position))
            }
        }
    }
    fun submitList(courselist: List<CoursesModel>){
        courses = courselist
    }
    inner class courseViewHolder(itemView: View) :
        RecyclerView.ViewHolder(itemView) {
        /*
        init {
            itemView.setOnClickListener {
                Toast.makeText(itemView.context,
                    itemView.course_id.text, Toast.LENGTH_SHORT).show()
            }
        }
         */
            val courseCode = itemView.course_id

            fun bind(courseModel:CoursesModel){
                courseCode.setText(courseModel.getcode())
            }
    }
}