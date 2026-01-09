from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .models import Student, Teacher, Course

# ----------------- HELPER FUNCTION -----------------
def get_json_body(request):
    """Safely parse JSON body"""
    try:
        return json.loads(request.body)
    except json.JSONDecodeError:
        return {}

# ----------------- STUDENT VIEWS -----------------
@csrf_exempt
@require_http_methods(["GET", "POST", "PATCH", "DELETE"])
def students_view(request, student_id=None):
    try:
        if request.method == "GET":
            if student_id:
                try:
                    student = Student.objects.get(id=student_id)
                    data = {
                        "id": student.id,
                        "first_name": student.first_name,
                        "last_name": student.last_name,
                        "email": student.email
                    }
                except Student.DoesNotExist:
                    return JsonResponse({"error": "Student not found"}, status=404)
            else:
                students = list(Student.objects.values())
                data = {"students": students}
            return JsonResponse(data)

        elif request.method == "POST":
            data = get_json_body(request)
            student = Student.objects.create(
                first_name=data.get("first_name", ""),
                last_name=data.get("last_name", ""),
                email=data.get("email", "")
            )
            return JsonResponse({"message": "Student created", "id": student.id}, status=201)

        elif request.method == "PATCH":
            if not student_id:
                return JsonResponse({"error": "Student ID required"}, status=400)
            data = get_json_body(request)
            try:
                student = Student.objects.get(id=student_id)
                student.first_name = data.get("first_name", student.first_name)
                student.last_name = data.get("last_name", student.last_name)
                student.email = data.get("email", student.email)
                student.save()
                return JsonResponse({"message": "Student updated"})
            except Student.DoesNotExist:
                return JsonResponse({"error": "Student not found"}, status=404)

        elif request.method == "DELETE":
            if not student_id:
                return JsonResponse({"error": "Student ID required"}, status=400)
            try:
                student = Student.objects.get(id=student_id)
                student.delete()
                return JsonResponse({"message": "Student deleted"})
            except Student.DoesNotExist:
                return JsonResponse({"error": "Student not found"}, status=404)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


# ----------------- TEACHER VIEWS -----------------
@csrf_exempt
@require_http_methods(["GET", "POST", "PATCH", "DELETE"])
def teachers_view(request, teacher_id=None):
    try:
        if request.method == "GET":
            if teacher_id:
                try:
                    teacher = Teacher.objects.get(id=teacher_id)
                    data = {
                        "id": teacher.id,
                        "first_name": teacher.first_name,
                        "last_name": teacher.last_name,
                        "email": teacher.email
                    }
                except Teacher.DoesNotExist:
                    return JsonResponse({"error": "Teacher not found"}, status=404)
            else:
                teachers = list(Teacher.objects.values())
                data = {"teachers": teachers}
            return JsonResponse(data)

        elif request.method == "POST":
            data = get_json_body(request)
            teacher = Teacher.objects.create(
                first_name=data.get("first_name", ""),
                last_name=data.get("last_name", ""),
                email=data.get("email", "")
            )
            return JsonResponse({"message": "Teacher created", "id": teacher.id}, status=201)

        elif request.method == "PATCH":
            if not teacher_id:
                return JsonResponse({"error": "Teacher ID required"}, status=400)
            data = get_json_body(request)
            try:
                teacher = Teacher.objects.get(id=teacher_id)
                teacher.first_name = data.get("first_name", teacher.first_name)
                teacher.last_name = data.get("last_name", teacher.last_name)
                teacher.email = data.get("email", teacher.email)
                teacher.save()
                return JsonResponse({"message": "Teacher updated"})
            except Teacher.DoesNotExist:
                return JsonResponse({"error": "Teacher not found"}, status=404)

        elif request.method == "DELETE":
            if not teacher_id:
                return JsonResponse({"error": "Teacher ID required"}, status=400)
            try:
                teacher = Teacher.objects.get(id=teacher_id)
                teacher.delete()
                return JsonResponse({"message": "Teacher deleted"})
            except Teacher.DoesNotExist:
                return JsonResponse({"error": "Teacher not found"}, status=404)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


# ----------------- COURSE VIEWS -----------------
@csrf_exempt
@require_http_methods(["GET", "POST", "PATCH", "DELETE"])
def courses_view(request, course_id=None):
    try:
        if request.method == "GET":
            if course_id:
                try:
                    course = Course.objects.get(id=course_id)
                    data = {
                        "id": course.id,
                        "name": course.name,
                        "description": course.description
                    }
                except Course.DoesNotExist:
                    return JsonResponse({"error": "Course not found"}, status=404)
            else:
                courses = list(Course.objects.values())
                data = {"courses": courses}
            return JsonResponse(data)

        elif request.method == "POST":
            data = get_json_body(request)
            course = Course.objects.create(
                name=data.get("name", ""),
                description=data.get("description", "")
            )
            return JsonResponse({"message": "Course created", "id": course.id}, status=201)

        elif request.method == "PATCH":
            if not course_id:
                return JsonResponse({"error": "Course ID required"}, status=400)
            data = get_json_body(request)
            try:
                course = Course.objects.get(id=course_id)
                course.name = data.get("name", course.name)
                course.description = data.get("description", course.description)
                course.save()
                return JsonResponse({"message": "Course updated"})
            except Course.DoesNotExist:
                return JsonResponse({"error": "Course not found"}, status=404)

        elif request.method == "DELETE":
            if not course_id:
                return JsonResponse({"error": "Course ID required"}, status=400)
            try:
                course = Course.objects.get(id=course_id)
                course.delete()
                return JsonResponse({"message": "Course deleted"})
            except Course.DoesNotExist:
                return JsonResponse({"error": "Course not found"}, status=404)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
