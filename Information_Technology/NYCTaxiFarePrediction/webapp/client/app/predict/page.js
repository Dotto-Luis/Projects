import Image from 'next/image';

export default function Predict() {
  return (
    <div className='container result-container mt-5 mx-auto max-w-md'>
      <h2 className='mb-4 text-yellow-500'>Prediction Result</h2>

      <div className='mb-3'>
        <label htmlFor='fare' className='form-label'>
          Predicted Fare:
        </label>
        <p className='text-xl font-semibold'>10</p>
      </div>

      <div className='mb-3'>
        <label htmlFor='duration' className='form-label'>
          Predicted Duration:
        </label>
        <p className='text-xl font-semibold'>20</p>
      </div>
    </div>
  );
}
