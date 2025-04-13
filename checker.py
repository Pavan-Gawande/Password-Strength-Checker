import string


class PasswordChecker: 
    def __init__(self, password):
        self.password = password
        self.length = len(password)

    def check_strength(self):
        has_lower = any(c.islower() for c in self.password)
        has_upper = any(c.isupper() for c in self.password)
        has_digit = any(c.isdigit() for c in self.password)
        has_special = any(c in string.punctuation for c in self.password)

        score = 0
        if self.length >= 8:
            score += 1
        if has_lower and has_upper:
            score += 1
        if has_digit:
            score += 1
        if has_special:
            score += 1
        if self.length >= 12:
            score += 1

        if score <= 2:
            strength = "Weak"
        elif score == 3:
            strength = "Moderate"
        else:
            strength = "Strong"

        return strength, self.estimate_crack_time()

    def estimate_crack_time(self):
        total_chars = ""
        if any(c.islower() for c in self.password):
            total_chars += string.ascii_lowercase
        if any(c.isupper() for c in self.password):
            total_chars += string.ascii_uppercase
        if any(c.isdigit() for c in self.password):
            total_chars += string.digits
        if any(c in string.punctuation for c in self.password):
            total_chars += string.punctuation
        
        base = len(total_chars)
        total_chars_pos = {ch:i+1 for i, ch in enumerate(total_chars)}
        
        final_position = 0
        for i, ch in enumerate(self.password):
            power = self.length - i - 1
            final_position += total_chars_pos.get(ch, 0) * (base ** power)
        
        guesses_per_sec = 1e9  # 1 billion/sec
        seconds = final_position / guesses_per_sec

        return self.convert_seconds(seconds)

    def convert_seconds(self, seconds):
        minutes, sec = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        years, days = divmod(days, 365)
        if years >= 1:
            return f"~{int(years)} years"
        elif days >= 1:
            return f"~{int(days)} days"
        elif hours >= 1:
            return f"~{int(hours)} hours"
        elif minutes >= 1:
            return f"~{int(minutes)} minutes"
        else:
            return f"~{int(sec)} seconds"