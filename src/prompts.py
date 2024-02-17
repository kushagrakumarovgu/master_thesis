
human_template = """ Below you will find a scientific peer review. Such review generally contain the reviewer's sentiment
in the first paragraph(s) of the review, followed by a list of specific recommendations to the authors. can you please review on
1. the sentiment, on a scale from -100 (negative) to 0 (neutral) to 100 (positive)
2. the politeness of the language use, on a scale from -100 (rude) to 0 (neutral) to 100 (polite)
3. Include a reasoning of how you established the score.
```{review}```
The output should be in JSON format. Please find the format instructions below.
```{format_instructions}```
"""
