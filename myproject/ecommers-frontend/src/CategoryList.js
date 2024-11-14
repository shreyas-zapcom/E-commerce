import { useEffect, useState } from "react";
import { getCategories } from "./ShopService"; // Adjust the path if necessary
import './CategoryList.css'; // Import a CSS file for styling (optional)

const CategoryList = () => {
    const [categories, setCategories] = useState([]);
    const [loading, setLoading] = useState(true); // Loading state
    const [error, setError] = useState(null); // Error state

    useEffect(() => {
        getCategories()
            .then((response) => {
                setCategories(response.data);
                setLoading(false); // Set loading to false once data is fetched
            })
            .catch((error) => {
                console.error("Error fetching categories:", error);
                setError("Failed to load categories. Please try again."); // Set error message
                setLoading(false); // Set loading to false even on error
            });
    }, []);

    if (loading) {
        return <div > Loading categories... < /div>; / / Loading message
    }

    if (error) {
        return <div > { error } < /div>; / / Error message
    }

    return ( <
            div className = "category-list" > { /* Add a class for styling */ } <
            h2 > Categories < /h2> {
            categories.length > 0 ? (
                categories.map((category) => ( <
                    div key = { category.id }
                    className = "category-item" > { /* Add a class for individual items */ } <
                    h3 > { category.name } < /h3> < /
                    div >
                ))
            ) : ( <
                div > No categories available. < /div> / / Message when there are no categories
            )
        } <
        /div>
);
};

export default CategoryList;