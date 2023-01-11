CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE avg_score DECIMAL(5, 2);
    SET avg_score = (SELECT AVG(score) FROM corrections WHERE user_id = user_id);
    UPDATE users SET average_score = avg_score WHERE id = user_id;
END;