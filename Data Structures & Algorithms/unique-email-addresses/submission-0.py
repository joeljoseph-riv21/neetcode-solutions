class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        inbox = set()

        for email in emails:
            local, domain = email.split('@', 1) # the word is extracted, before first @ symbol.

            local = local.split('+', 1)[0].replace('.', '') # splits text from first '+' into 2 parts then, extracts the first word [0].
            inbox.add(f"{local}@{domain}")
        return len(inbox) # explicitely return the length of unique emails.
        