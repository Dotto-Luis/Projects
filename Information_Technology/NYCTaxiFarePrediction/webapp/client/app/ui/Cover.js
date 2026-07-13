const Cover = () => {
  return (
    <>
      <div className='hero-cover relative bg-cover bg-center min-h-[50vh]'>
        <div className='color-overlay absolute inset-0 bg-black bg-opacity-20 flex justify-center items-center text-center'>
          <h1 className='text-white  text-2xl sm:text-3xl md:text-4xl lg:text-5xl xl:text-6xl'>
            NYC Taxi Fare and Trip Duration Prediction
          </h1>
        </div>
      </div>
    </>
  );
};

export default Cover;
