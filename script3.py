def ContinueCurse():
    test_note_1 = (int(input("Type first Test Value: ")))
    test_note_2 = (int(input("Type Second Test Value: "))) 
    tmp_note = (((test_note_1 + test_note_2)/2)*0.6)
    if ((3 - tmp_note)/0.4) <= 5:
         print "Keep Studying :D"
    else:
         print "Cancel course :/"
    print "=== Program Finished ==="

print " ==== Starting the -ContinueCourse- Script ===="
ContinueCurse()
