import math

def square_diff (x, y) :
    return (x - y) ** 2

def computeRMSE(probeAnswers, probeEstimate) :
    count = 0
    sum = 0.0
    while True:
        answers_line    = probeAnswers.readline().rstrip("\n")
        estimate_line   = probeEstimate.readline().rstrip("\n")
        if answers_line == "":
            break
        elif not ":" in answers_line: # If it's not a movieID, then compare ratings
            answer_rating       = int(answers_line)
            estimated_rating    = float(estimate_line)
            sum     += square_diff(answer_rating, estimated_rating)
            count   += 1
    return math.sqrt(sum/count)

# Compute the RMSE
probeEstimated = open('ProbeEstimated.txt', 'r')
probeAnswers = open("data/ProbeAnswers.txt", 'r')
print computeRMSE(probeAnswers, probeEstimated)
probeAnswers.close()