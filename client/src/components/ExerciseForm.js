import { useEffect, useState } from "react";

function ExerciseForm({ workoutId, onAddExercise }) {
  const [exercises, setExercises] = useState([]);
  const [exerciseId, setExerciseId] = useState("");
  const [sets, setSets] = useState("");
  const [reps, setReps] = useState("");
  const [formErrors, setFormErrors] = useState([]);

  useEffect(() => {
    fetch("/exercises")
      .then((r) => r.json())
      .then(setExercises);
  }, []);

  function handleSubmit(e) {
    e.preventDefault();
    const formData = {
      exercise_id: exerciseId,
      workout_id: workoutId,
      sets,
      reps,
    };
    fetch("/workout_exercises", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    }).then((r) => {
      if (r.ok) {
        r.json().then((newWorkoutExercise) => {
          onAddExercise(newWorkoutExercise);
          setFormErrors([]);
        });
      } else {
        r.json().then((err) => setFormErrors(err.errors));
      }
    });
  }

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="exercise_id">Exercise:</label>
      <select
        id="exercise_id"
        name="exercise_id"
        value={exerciseId}
        onChange={(e) => setExerciseId(e.target.value)}
      >
        <option value="">Select an exercise</option>
        {exercises.map((exercise) => (
          <option key={exercise.id} value={exercise.id}>
            {exercise.name}
          </option>
        ))}
      </select>
      <label htmlFor="sets">Sets:</label>
      <input
        id="sets"
        name="sets"
        type="number"
        value={sets}
        onChange={(e) => setSets(parseInt(e.target.value))}
      />
      <label htmlFor="reps">Reps:</label>
      <input
        id="reps"
        name="reps"
        type="number"
        value={reps}
        onChange={(e) => setReps(parseInt(e.target.value))}
      />
      {formErrors.length > 0 &&
        formErrors.map((err) => (
          <p key={err} style={{ color: "red" }}>
            {err}
          </p>
        ))}
      <button type="submit">Add Exercise</button>
    </form>
  );
}

export default ExerciseForm;
