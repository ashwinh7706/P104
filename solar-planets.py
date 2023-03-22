import cv2

solarsystem = cv2.imread("solar-system.jpg")

cv2.putText(solarsystem,
             "Sun",
               (20,300),
                 cv2.FONT_HERSHEY_COMPLEX
                 ,
                   0.5,
                     (255,255,255))

cv2.putText(solarsystem,
             "Mercury",
               (80,230),
                 cv2.FONT_HERSHEY_COMPLEX
                 ,
                   0.5,
                     (255,255,255))

cv2.putText(solarsystem,
             "Venus",
               (200,230),
                 cv2.FONT_HERSHEY_COMPLEX
                 ,
                   0.5,
                     (255,255,255))

cv2.putText(solarsystem,
             "Earth",
               (300,230),
                 cv2.FONT_HERSHEY_COMPLEX
                 ,
                   0.5,
                     (255,255,255))

cv2.putText(solarsystem,
             "Mars",
               (400,230),
                 cv2.FONT_HERSHEY_COMPLEX
                 ,
                   0.5,
                     (255,255,255))

cv2.putText(solarsystem,
             "Jupiter",
               (600,230),
                 cv2.FONT_HERSHEY_COMPLEX
                 ,
                   0.5,
                     (255,255,255))

cv2.putText(solarsystem,
             "Saturn",
               (800,230),
                 cv2.FONT_HERSHEY_COMPLEX
                 ,
                   0.5,
                     (255,255,255))

cv2.putText(solarsystem,
             "Uranus",
               (1000,230),
                 cv2.FONT_HERSHEY_COMPLEX
                 ,
                   0.5,
                     (255,255,255))

cv2.putText(solarsystem,
             "Neptune",
               (1100,230),
                 cv2.FONT_HERSHEY_COMPLEX
                 ,
                   0.5,
                     (255,255,255))

cv2.imshow("solar system", solarsystem)

cv2.waitKey(0)

cv2.imwrite("Solar_systemwithname.jpg", solarsystem)



