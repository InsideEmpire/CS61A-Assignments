test = {
  'name': 'Question 0',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> test_dice = make_test_dice(4, 1, 2)
          >>> test_dice()
          8173f986869be686c354ef4558841f7c
          # locked
          >>> test_dice() # Second call
          c4933a0dd093653b499b3bff4a4c8ec8
          # locked
          >>> test_dice() # Third call
          62a329e8634e8fe7dd0b7f2080aba699
          # locked
          >>> test_dice() # Fourth call
          8173f986869be686c354ef4558841f7c
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'answer': '3f4d6d6f24c125040335c759e632092f',
          'choices': [
            'make_test_dice(6)',
            'make_fair_dice(6)',
            'six_sided',
            'six_sided()',
            'six_sided(1)',
            'six_sided(6)'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'Which of the following is the correct way to "roll" a fair, six-sided die?'
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
