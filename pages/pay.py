import razorpay as rp


class cli:
    client=rp.Client(auth=("rzp_test_nVCGLmk60BozNk", "uByP3i0XSY33cKL3eNW6KTL1"))
    client.set_app_details({"title" : "Onemail", "version" : "1.0"})
    