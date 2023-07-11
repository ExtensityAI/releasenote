from symai import Expression, Function


FUNCTION_DESCRIPTION = '''
Write a {template} release note based on the changelog from the GitHub repository commits. Don't explicitly write the users or dates, just the changes in logical groups.
'''


class ReleaseNote(Expression):
    def __init__(self):
        super().__init__()
        self.fn = Function(FUNCTION_DESCRIPTION)

    def forward(self, data, template: str = 'Markdown'):
        data = self._to_symbol(data)
        self.fn.format(template=template)
        return self.fn(data)
