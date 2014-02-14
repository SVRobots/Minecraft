def Render3D():
	width, height = window.get_size()
	glEnable(GL_DEPTH_TEST)
	glViewport(0, 0, width, height)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(65.0, width / float(height), 0.1, 60.0)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()

