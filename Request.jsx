import React, { useState } from 'react';

const CodeGenerator = () => {
  const [userInput, setUserInput] = useState('');
  const [generatedCode, setGeneratedCode] = useState('');

  const generateCode = async () => {
    try {
      const response = await fetch('http://localhost:5000/generate-code', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ input: userInput }),
      });

      const data = await response.json();
      setGeneratedCode(data.generatedCode);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <textarea
        placeholder="Enter your code generation prompt..."
        value={userInput}
        onChange={(e) => setUserInput(e.target.value)}
      />
      <button onClick={generateCode}>Generate Code</button>
      <div>
        <h3>Generated Code:</h3>
        <pre>{generatedCode}</pre>
      </div>
    </div>
  );
};

export default CodeGenerator;
